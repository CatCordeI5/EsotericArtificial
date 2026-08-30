import puppeteer from 'puppeteer';
import http from 'http';

const PORT = 8765;

console.log("[.noia] Initializing Lunoia browser bridge...");

async function scrapeWithBrowser(url) {
  const browser = await puppeteer.launch({ 
    headless: "new", 
    args: ['--no-sandbox', '--disable-setuid-sandbox'] 
  });
  const page = await browser.newPage();
  
  await page.setUserAgent('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36');
  
  console.log(`[.noia] Diving into: ${url}`);
  await page.goto(url, { waitUntil: 'networkidle2' });

  const content = await page.evaluate(() => document.body.innerText);
  
  await browser.close();
  return content;
}

const server = http.createServer(async (req, res) => {
  if (req.method === 'POST' && req.url === '/hook') {
    let body = '';
    req.on('data', chunk => { body += chunk.toString(); });
    req.on('end', async () => {
      try {
        const { url } = JSON.parse(body);
        const data = await scrapeWithBrowser(url);
        
        res.writeHead(200, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ status: 'success', data: data.substring(0, 2000) }));
      } catch (error) {
        res.writeHead(500, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ status: 'error', message: error.message }));
      }
    });
  } else {
    res.writeHead(404);
    res.end('Not Found');
  }
});

server.listen(PORT, () => {
  console.log(`[.noia] Listening on http://localhost:${PORT}. Waiting for Lunoia...`);
});
