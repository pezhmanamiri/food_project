const cacheName = 'food-cache-v1';
const staticAssets = [
  '/',
  '/login/',
  '/select/',
  '/summary/',
  '/static/css/styles.css',
  '/static/js/sw.js'
];

self.addEventListener('install', async e => {
  const cache = await caches.open(cacheName);
  await cache.addAll(staticAssets);
  return self.skipWaiting();
});

self.addEventListener('activate', e => {
  self.clients.claim();
});

self.addEventListener('fetch', async e => {
  const req = e.request;
  const cachedResponse = await caches.match(req);
  return cachedResponse || fetch(req);
});
