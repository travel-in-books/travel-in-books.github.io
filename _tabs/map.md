---
layout: page
title: نقشه جهانی
icon: fas fa-globe
order: 5
---

<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" integrity="sha256-p4NxAoJBhIIN+hmNHrzRCf9tD/miZyoHS5obTRR9BMY=" crossorigin=""/>
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js" integrity="sha256-20nQCchB9co0qIjJZRGuk2/Z9VM+kNiyxNV/XN/WPeE=" crossorigin=""></script>

<style>
  #book-map {
    height: 520px;
    width: 100%;
    border-radius: 8px;
    margin-bottom: 1.5rem;
    z-index: 0;
  }
  .map-legend {
    background: var(--card-bg, #fff);
    border: 1px solid var(--border-color, #ddd);
    border-radius: 8px;
    padding: 0.8rem 1rem;
    font-size: 0.85rem;
    display: flex;
    flex-wrap: wrap;
    gap: 0.6rem 1.2rem;
    align-items: center;
    direction: rtl;
  }
  .legend-item {
    display: flex;
    align-items: center;
    gap: 0.4rem;
  }
  .legend-circle {
    border-radius: 50%;
    background: rgba(214, 69, 52, 0.65);
    border: 1.5px solid #c0392b;
    flex-shrink: 0;
  }
  .leaflet-popup-content b { font-size: 1rem; }
  .leaflet-popup-content ul {
    margin: 0.4rem 0 0;
    padding-right: 1.1rem;
    padding-left: 0;
    list-style: disc;
    max-height: 200px;
    overflow-y: auto;
  }
  .leaflet-popup-content ul li { margin: 2px 0; }
  .leaflet-popup-content a { color: #c0392b; }
</style>

<div id="book-map"></div>

<div class="map-legend">
  <span style="font-weight:600;">تعداد کتاب‌ها:</span>
  <span class="legend-item"><span class="legend-circle" style="width:10px;height:10px;"></span> ۱–۲</span>
  <span class="legend-item"><span class="legend-circle" style="width:16px;height:16px;"></span> ۳–۶</span>
  <span class="legend-item"><span class="legend-circle" style="width:24px;height:24px;"></span> ۷–۱۵</span>
  <span class="legend-item"><span class="legend-circle" style="width:34px;height:34px;"></span> ۱۶+</span>
</div>

<script>
const coords = {
  "آمریکا":         [37.090, -95.713],
  "انگلیس":         [52.355,  -1.174],
  "روسیه":          [61.524, 105.319],
  "ژاپن":           [36.205, 138.253],
  "فرانسه":         [46.228,   2.214],
  "ایران":          [32.428,  53.688],
  "آرژانتین":       [-38.416, -63.617],
  "ایتالیا":        [41.872,  12.567],
  "آلمان":          [51.166,  10.452],
  "سوئیس":          [46.818,   8.228],
  "نیجریه":         [ 9.082,   8.675],
  "مکزیک":          [23.635, -102.553],
  "کلمبیا":         [ 4.571, -74.297],
  "کانادا":         [56.130, -106.347],
  "پرو":            [-9.190, -75.015],
  "ایرلند":         [53.142,  -7.692],
  "مصر":            [26.821,  30.803],
  "لهستان":         [51.919,  19.145],
  "کره":            [35.908, 127.767],
  "شیلی":           [-35.675, -71.543],
  "سوئد":           [60.128,  18.644],
  "سریلانکا":       [ 7.873,  80.772],
  "چین":            [35.862, 104.195],
  "ترکیه":          [38.964,  35.243],
  "برزیل":          [-14.235, -51.925],
  "استرالیا":       [-25.274, 133.775],
  "اسپانیا":        [40.464,  -3.749],
  "آفریقای جنوبی":  [-30.560,  22.938]
};

const countryData = [
  {% assign country_list = "آمریکا,انگلیس,روسیه,ژاپن,فرانسه,ایران,آرژانتین,ایتالیا,آلمان,سوئیس,نیجریه,مکزیک,کلمبیا,کانادا,پرو,ایرلند,مصر,لهستان,کره,شیلی,سوئد,سریلانکا,چین,ترکیه,برزیل,استرالیا,اسپانیا,آفریقای جنوبی" | split: "," %}
  {% for country in country_list %}
    {% assign posts_in_country = site.tags[country] %}
    {% assign count = posts_in_country | size %}
    {% if count > 0 %}
  {
    name: {{ country | jsonify }},
    count: {{ count }},
    books: [{% for post in posts_in_country %}{ title: {{ post.title | jsonify }}, url: {{ post.url | jsonify }} }{% unless forloop.last %},{% endunless %}{% endfor %}]
  },
    {% endif %}
  {% endfor %}
];

const map = L.map('book-map', { zoomControl: true }).setView([25, 15], 2);

L.tileLayer('https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png', {
  attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> &copy; <a href="https://carto.com/">CARTO</a>',
  subdomains: 'abcd',
  maxZoom: 19
}).addTo(map);

countryData.forEach(d => {
  const latlng = coords[d.name];
  if (!latlng) return;

  const radius = 5 + Math.sqrt(d.count) * 5;

  const bookListHTML = d.books
    .map(b => `<li><a href="${b.url}" target="_blank">${b.title}</a></li>`)
    .join('');

  const popup = `<b>${d.name}</b> — ${d.count} کتاب<ul>${bookListHTML}</ul>`;

  L.circleMarker(latlng, {
    radius: radius,
    fillColor: '#d64534',
    color: '#9b1c0e',
    weight: 1.5,
    fillOpacity: 0.65,
  })
  .addTo(map)
  .bindPopup(popup, { maxWidth: 280, maxHeight: 320 });
});
</script>
