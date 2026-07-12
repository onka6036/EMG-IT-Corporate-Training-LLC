import { getAssetFromKV } from '@cloudflare/kv-asset-handler';

addEventListener('fetch', event => {
  event.respondWith(handleEvent(event));
});

async function handleEvent(event) {
  return getAssetFromKV(event, {
    mapRequestToAsset: request => {
      const url = new URL(request.url);
      // If the path is the root or already ends with '/', serve index.html in that directory
      if (url.pathname === '/' || url.pathname.endsWith('/')) {
        return new Request(`${url.origin}${url.pathname}index.html`, request);
      }

      // If the path has a file extension (e.g., .css, .js, .png), return original request
      const lastSegment = url.pathname.split('/').pop() || '';
      if (lastSegment.includes('.')) {
        return request;
      }

      // Otherwise, map requests like '/about' to '/about/index.html'
      return new Request(`${url.origin}${url.pathname}/index.html`, request);
    }
  });
}
