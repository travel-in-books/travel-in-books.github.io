---
layout: page
title: خط زمانی
icon: fas fa-stream
order: 6
---

<style>
  .tl-summary {
    font-size: 0.85rem;
    color: #888;
    margin-bottom: 1.2rem;
    direction: rtl;
  }

  /* Column labels */
  .tl-col-labels {
    display: grid;
    grid-template-columns: 1fr 1fr;
    direction: ltr;
    margin-bottom: 0.8rem;
  }
  .tl-col-label {
    font-size: 0.7rem;
    font-weight: 700;
    letter-spacing: 0.05em;
    color: #bbb;
    text-transform: uppercase;
    direction: rtl;
  }
  .tl-col-label.hist { padding-right: 1rem; }
  .tl-col-label.books { padding-left: 1rem; }

  /* Outer container — holds the center line as a pseudo-element */
  .tl-container {
    position: relative;
  }
  .tl-container::before {
    content: '';
    position: absolute;
    left: 50%;
    transform: translateX(-50%);
    top: 0;
    bottom: 0;
    width: 3px;
    background: var(--border-color, #dee2e6);
    z-index: 0;
  }

  /* One group per decade */
  .tl-decade-group {
    position: relative;
    margin-bottom: 2.5rem;
  }

  /* Red dot sitting on the center line */
  .tl-decade-dot {
    position: absolute;
    left: 50%;
    transform: translateX(-50%);
    top: 0.28rem;
    width: 13px;
    height: 13px;
    border-radius: 50%;
    background: #d64534;
    border: 2px solid var(--body-bg, #fff);
    box-shadow: 0 0 0 2px #d64534;
    z-index: 1;
  }

  /* Decade label centered above the two columns */
  .tl-decade-label {
    text-align: center;
    padding-top: 1.7rem;
    margin-bottom: 0.55rem;
    font-size: 1rem;
    font-weight: 700;
    color: #d64534;
    direction: rtl;
    position: relative;
    z-index: 1;
  }

  /* Two-column content row */
  .tl-content-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    direction: ltr;  /* explicit so col-1 = left, col-2 = right */
    position: relative;
    z-index: 1;
  }

  /* Left column: history events */
  .tl-hist-col {
    padding-right: 1.2rem;
    direction: rtl;
  }

  /* Right column: books */
  .tl-books-col {
    padding-left: 1.2rem;
    direction: rtl;
  }

  /* History event row */
  .tl-event {
    display: flex;
    align-items: baseline;
    gap: 0.45rem;
    padding: 0.18rem 0;
    direction: rtl;
  }
  .tl-event-year {
    font-size: 0.72rem;
    color: #ccc;
    white-space: nowrap;
    flex-shrink: 0;
  }
  .tl-event-text {
    font-size: 0.8rem;
    color: #888;
    line-height: 1.45;
  }

  /* Book row */
  .tl-book {
    display: flex;
    align-items: baseline;
    gap: 0.55rem;
    padding: 0.22rem 0;
    direction: rtl;
  }
  .tl-year {
    color: #888;
    white-space: nowrap;
    font-size: 0.8rem;
    min-width: 2.8rem;
    flex-shrink: 0;
  }
  .tl-title a {
    color: inherit;
    text-decoration: none;
    font-size: 0.9rem;
  }
  .tl-title a:hover {
    color: #d64534;
    text-decoration: underline;
  }
  .tl-country {
    font-size: 0.72rem;
    color: #aaa;
    white-space: nowrap;
  }

  /* Mobile: single column, books on top */
  @media (max-width: 640px) {
    .tl-container::before { display: none; }
    .tl-col-labels { display: none; }
    .tl-content-grid { grid-template-columns: 1fr; }
    .tl-books-col {
      order: 1;
      padding-left: 0;
      padding-right: 1.2rem;
      border-right: 3px solid var(--border-color, #dee2e6);
    }
    .tl-hist-col {
      order: 2;
      padding-right: 0;
      padding-top: 0.5rem;
      padding-bottom: 0.2rem;
      margin-top: 0.3rem;
      border-top: 1px dashed var(--border-color, #dee2e6);
    }
    .tl-decade-dot {
      left: unset;
      right: -1.65rem;
      transform: none;
    }
    .tl-decade-label { text-align: right; padding-top: 0; }
  }
</style>

<p class="tl-summary" id="tl-summary"></p>
<div class="tl-col-labels">
  <div class="tl-col-label hist">رویدادهای تاریخی</div>
  <div class="tl-col-label books">کتاب‌ها</div>
</div>
<div class="tl-container" id="tl-container"></div>

<script>
const books = [
  {% for post in site.posts %}
    {% unless post.path contains "template" %}
      {% assign after_rating = "" %}
      {% assign year_tag = "" %}
      {% for tag in post.tags %}
        {% if after_rating == "yes" and year_tag == "" %}
          {% assign year_tag = tag | strip %}
        {% endif %}
        {% if tag contains "⭐" or tag contains "☆" %}
          {% assign after_rating = "yes" %}
        {% endif %}
      {% endfor %}
      {% if year_tag != "" and year_tag != "۰۰۰۰" %}
        {% assign yr = year_tag | replace:"۰","0" | replace:"۱","1" | replace:"۲","2" | replace:"۳","3" | replace:"۴","4" | replace:"۵","5" | replace:"۶","6" | replace:"۷","7" | replace:"۸","8" | replace:"۹","9" | plus: 0 %}
        {% if yr > 0 %}
  { title: {{ post.title | jsonify }}, url: {{ post.url | jsonify }}, year: {{ yr }}, yearFa: {{ year_tag | jsonify }}, country: {{ post.tags | first | strip | jsonify }} },
        {% endif %}
      {% endif %}
    {% endunless %}
  {% endfor %}
];

/* Historical events keyed by decade (Math.floor(year/10)*10) */
const HISTORY = {
  1180: [{y:1187,t:'صلاح‌الدین ایوبی بیت‌المقدس را از صلیبیون بازپس می‌گیرد'},{y:1189,t:'جنگ صلیبی سوم آغاز می‌شود'}],
  1190: [{y:1192,t:'صلح ریچارد شیردل با صلاح‌الدین'}],
  1200: [{y:1206,t:'چنگیزخان امپراتوری مغول را بنیان می‌گذارد'},{y:1215,t:'امضای منشور کبیر (Magna Carta) در انگلیس'}],
  1220: [{y:1220,t:'مغولان به خراسان و ایران حمله می‌کنند'}],
  1240: [{y:1241,t:'مغولان لهستان و مجارستان را نابود می‌کنند'}],
  1250: [{y:1258,t:'سقوط بغداد به دست مغولان — پایان خلافت عباسی'},{y:1271,t:'مارکوپولو سفر به چین را آغاز می‌کند'}],
  1340: [{y:1347,t:'طاعون سیاه به اروپا می‌رسد — یک‌سوم جمعیت قاره می‌میرند'}],
  1360: [{y:1368,t:'سلسله مینگ در چین تأسیس می‌شود'}],
  1370: [{y:1370,t:'تیمورلنگ امپراتوری خود را در آسیای میانه بنا می‌گذارد'}],
  1400: [{y:1402,t:'تیمور سلطان بایزید عثمانی را در نبرد آنقره شکست می‌دهد'}],
  1430: [{y:1439,t:'گوتنبرگ چاپخانه را اختراع می‌کند'}],
  1450: [{y:1453,t:'سقوط قسطنطنیه — پایان امپراتوری بیزانس'}],
  1490: [{y:1492,t:'کریستف کلمب به قاره آمریکا می‌رسد'}],
  1500: [{y:1501,t:'شاه اسماعیل سلسله صفوی را در ایران تأسیس می‌کند'},{y:1517,t:'اصلاحات دینی مارتین لوتر'}],
  1540: [{y:1543,t:'کپرنیک نظریه خورشیدمرکزی را منتشر می‌کند'}],
  1570: [{y:1571,t:'نبرد لپانتو — ناوگان عثمانی شکست می‌خورد'}],
  1600: [{y:1600,t:'کمپانی هند شرقی بریتانیا تأسیس می‌شود'}],
  1610: [{y:1618,t:'جنگ سی‌ساله در اروپا آغاز می‌شود'}],
  1640: [{y:1648,t:'صلح وستفالی — پایان جنگ سی‌ساله'}],
  1680: [{y:1687,t:'نیوتن اصول ریاضی را منتشر می‌کند'}],
  1750: [{y:1756,t:'جنگ هفت‌ساله — نخستین جنگ جهانی واقعی'},{y:1769,t:'جیمز وات ماشین بخار را بهینه می‌کند'}],
  1770: [{y:1776,t:'اعلامیه استقلال آمریکا'}],
  1780: [{y:1789,t:'انقلاب کبیر فرانسه آغاز می‌شود'}],
  1800: [{y:1804,t:'ناپلئون بناپارت امپراتور فرانسه می‌شود'}],
  1810: [{y:1815,t:'شکست نهایی ناپلئون در واترلو'}],
  1820: [{y:1821,t:'استقلال یونان از امپراتوری عثمانی'}],
  1840: [{y:1848,t:'مانیفست کمونیست؛ انقلاب‌های سرتاسر اروپا'}],
  1850: [{y:1859,t:'داروین نظریه تکامل را منتشر می‌کند'}],
  1860: [{y:1865,t:'الغای برده‌داری در آمریکا'},{y:1869,t:'افتتاح کانال سوئز'}],
  1870: [{y:1871,t:'اتحاد دولت‌های آلمان'},{y:1876,t:'گراهام بل تلفن را اختراع می‌کند'}],
  1880: [{y:1884,t:'کنفرانس برلین — قدرت‌های اروپایی آفریقا را تقسیم می‌کنند'}],
  1890: [{y:1895,t:'برادران لومیر سینما را اختراع می‌کنند'}],
  1900: [{y:1903,t:'برادران رایت نخستین پرواز موفق را انجام می‌دهند'},{y:1905,t:'انیشتین نظریه نسبیت خاص را ارائه می‌کند'}],
  1910: [{y:1914,t:'آغاز جنگ جهانی اول'},{y:1917,t:'انقلاب روسیه — تأسیس اتحاد شوروی'}],
  1920: [{y:1928,t:'فلمینگ پنی‌سیلین را کشف می‌کند'},{y:1929,t:'بحران بزرگ اقتصادی آغاز می‌شود'}],
  1930: [{y:1936,t:'جنگ داخلی اسپانیا'},{y:1939,t:'آغاز جنگ جهانی دوم'}],
  1940: [{y:1945,t:'پایان جنگ جهانی دوم — بمب اتمی هیروشیما و ناگاساکی'},{y:1948,t:'تأسیس دولت اسرائیل'}],
  1950: [{y:1953,t:'واتسون و کریک ساختار مارپیچ DNA را کشف می‌کنند'},{y:1957,t:'شوروی اسپوتنیک را به فضا می‌فرستد'}],
  1960: [{y:1963,t:'ترور جان اف. کندی در دالاس'},{y:1969,t:'نیل آرمسترانگ روی ماه قدم می‌گذارد'}],
  1970: [{y:1973,t:'بحران نفتی — جنگ یوم کیپور'},{y:1979,t:'انقلاب اسلامی ایران'}],
  1980: [{y:1986,t:'فاجعه نیروگاه هسته‌ای چرنوبیل'},{y:1989,t:'سقوط دیوار برلین'}],
  1990: [{y:1991,t:'فروپاشی اتحاد جماهیر شوروی'},{y:1994,t:'پایان رژیم آپارتاید در آفریقای جنوبی'}],
  2000: [{y:2001,t:'حملات تروریستی ۱۱ سپتامبر'},{y:2008,t:'بحران مالی جهانی'}],
  2010: [{y:2011,t:'بهار عربی در شمال آفریقا و خاورمیانه'},{y:2016,t:'رأی‌گیری برگزیت در بریتانیا'}],
  2020: [{y:2020,t:'همه‌گیری جهانی کووید-۱۹'},{y:2022,t:'حمله روسیه به اوکراین'}],
};

function toPersian(n) {
  return String(n).replace(/[0-9]/g, d => '۰۱۲۳۴۵۶۷۸۹'[+d]);
}

books.sort((a, b) => a.year - b.year);

const groups = new Map();
for (const b of books) {
  const d = Math.floor(b.year / 10) * 10;
  if (!groups.has(d)) groups.set(d, []);
  groups.get(d).push(b);
}

document.getElementById('tl-summary').textContent =
  `${toPersian(books.length)} کتاب از ${toPersian(books[0].year)} تا ${toPersian(books[books.length-1].year)}`;

const container = document.getElementById('tl-container');

for (const [decade, decadeBooks] of groups) {
  const events = HISTORY[decade] || [];

  const group = document.createElement('div');
  group.className = 'tl-decade-group';

  const dot = document.createElement('div');
  dot.className = 'tl-decade-dot';
  group.appendChild(dot);

  const label = document.createElement('div');
  label.className = 'tl-decade-label';
  label.textContent = `دهه ${toPersian(decade)}`;
  group.appendChild(label);

  const grid = document.createElement('div');
  grid.className = 'tl-content-grid';

  /* Left column: historical events */
  const histCol = document.createElement('div');
  histCol.className = 'tl-hist-col';
  if (events.length === 0) {
    const dash = document.createElement('span');
    dash.style.cssText = 'color:#ddd;font-size:0.72rem';
    dash.textContent = '—';
    histCol.appendChild(dash);
  } else {
    for (const ev of events) {
      const row = document.createElement('div');
      row.className = 'tl-event';
      const yr = document.createElement('span');
      yr.className = 'tl-event-year';
      yr.textContent = toPersian(ev.y);
      const txt = document.createElement('span');
      txt.className = 'tl-event-text';
      txt.textContent = ev.t;
      row.appendChild(yr);
      row.appendChild(txt);
      histCol.appendChild(row);
    }
  }

  /* Right column: books */
  const booksCol = document.createElement('div');
  booksCol.className = 'tl-books-col';
  for (const b of decadeBooks) {
    const row = document.createElement('div');
    row.className = 'tl-book';
    const year = document.createElement('span');
    year.className = 'tl-year';
    year.textContent = b.yearFa;
    const title = document.createElement('span');
    title.className = 'tl-title';
    const link = document.createElement('a');
    link.href = b.url;
    link.textContent = b.title;
    title.appendChild(link);
    const country = document.createElement('span');
    country.className = 'tl-country';
    country.textContent = b.country;
    row.appendChild(year);
    row.appendChild(title);
    row.appendChild(country);
    booksCol.appendChild(row);
  }

  grid.appendChild(histCol);
  grid.appendChild(booksCol);
  group.appendChild(grid);
  container.appendChild(group);
}
</script>
