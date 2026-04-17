---
# the default layout is 'page'
icon: fas fa-info-circle
order: 4
---

اینجا برای وقایع‌نگاری داستان‌خوانی‌ام است. می‌تواند خلاصه داستان یا بخشی از داستان یا شاید فقط شخصیت‌های داستان باشد.

> در حال حاضر دارم نظراتم رو راجب کتاب‌ها جمع می‌کنم. :)
{: .prompt-tip }

---

{% assign total = site.posts | size %}
{% assign country_list = "آمریکا,انگلیس,روسیه,ژاپن,فرانسه,ایران,آرژانتین,ایتالیا,آلمان,سوئیس,نیجریه,مکزیک,کلمبیا,کانادا,پرو,ایرلند,مصر,لهستان,کره,شیلی,سوئد,اسپانیا,آفریقای جنوبی,برزیل,ترکیه,سریلانکا,استرالیا,چین" | split: "," %}
{% assign country_count = country_list | size %}

{% assign novel_count = 0 %}
{% assign short_count = 0 %}
{% assign nonfic_count = 0 %}
{% assign other_count = 0 %}
{% for post in site.posts %}
  {% unless post.path contains 'template' %}
    {% assign cat_str = post.categories | join: "," %}
    {% if cat_str contains 'رمان' %}
      {% assign novel_count = novel_count | plus: 1 %}
    {% elsif cat_str contains 'داستان کوتاه' %}
      {% assign short_count = short_count | plus: 1 %}
    {% elsif cat_str contains 'غیر' %}
      {% assign nonfic_count = nonfic_count | plus: 1 %}
    {% else %}
      {% assign other_count = other_count | plus: 1 %}
    {% endif %}
  {% endunless %}
{% endfor %}

{% assign r10=0 %}{% assign r9=0 %}{% assign r8=0 %}{% assign r7=0 %}{% assign r6=0 %}
{% assign r5=0 %}{% assign r4=0 %}{% assign r3=0 %}{% assign r2=0 %}{% assign r1=0 %}
{% assign rated_count = 0 %}{% assign rating_sum = 0 %}
{% for post in site.posts %}
  {% unless post.path contains 'template' %}
    {% for tag in post.tags %}
      {% if tag contains '/10' %}
        {% assign sc = tag | split: ' ' | last | split: '/' | first %}
        {% if sc == '10' %}{% assign r10 = r10 | plus: 1 %}{% assign rated_count = rated_count | plus: 1 %}{% assign rating_sum = rating_sum | plus: 10 %}
        {% elsif sc == '9' %}{% assign r9 = r9 | plus: 1 %}{% assign rated_count = rated_count | plus: 1 %}{% assign rating_sum = rating_sum | plus: 9 %}
        {% elsif sc == '8' %}{% assign r8 = r8 | plus: 1 %}{% assign rated_count = rated_count | plus: 1 %}{% assign rating_sum = rating_sum | plus: 8 %}
        {% elsif sc == '7' %}{% assign r7 = r7 | plus: 1 %}{% assign rated_count = rated_count | plus: 1 %}{% assign rating_sum = rating_sum | plus: 7 %}
        {% elsif sc == '6' %}{% assign r6 = r6 | plus: 1 %}{% assign rated_count = rated_count | plus: 1 %}{% assign rating_sum = rating_sum | plus: 6 %}
        {% elsif sc == '5' %}{% assign r5 = r5 | plus: 1 %}{% assign rated_count = rated_count | plus: 1 %}{% assign rating_sum = rating_sum | plus: 5 %}
        {% elsif sc == '4' %}{% assign r4 = r4 | plus: 1 %}{% assign rated_count = rated_count | plus: 1 %}{% assign rating_sum = rating_sum | plus: 4 %}
        {% elsif sc == '3' %}{% assign r3 = r3 | plus: 1 %}{% assign rated_count = rated_count | plus: 1 %}{% assign rating_sum = rating_sum | plus: 3 %}
        {% elsif sc == '2' %}{% assign r2 = r2 | plus: 1 %}{% assign rated_count = rated_count | plus: 1 %}{% assign rating_sum = rating_sum | plus: 2 %}
        {% elsif sc == '1' %}{% assign r1 = r1 | plus: 1 %}{% assign rated_count = rated_count | plus: 1 %}{% assign rating_sum = rating_sum | plus: 1 %}
        {% endif %}
      {% endif %}
    {% endfor %}
  {% endunless %}
{% endfor %}
{% assign avg_x10 = rating_sum | times: 10 | divided_by: rated_count %}
{% assign avg_int = avg_x10 | divided_by: 10 %}
{% assign avg_dec = avg_x10 | modulo: 10 %}

<style>
.stat-cards {
  display: flex;
  gap: 1rem;
  margin: 1.5rem 0;
  flex-wrap: wrap;
}
.stat-card {
  flex: 1;
  min-width: 120px;
  border: 1px solid var(--border-color, #ddd);
  border-radius: 8px;
  padding: 1rem;
  text-align: center;
}
.stat-card .num {
  font-size: 2rem;
  font-weight: bold;
  color: var(--link-color, #0070f3);
  display: block;
  direction: ltr;
}
.stat-card .label {
  font-size: 0.85rem;
  opacity: 0.75;
}
.stats-section { margin: 2rem 0; }
.stats-section h3 { margin-bottom: 0.75rem; font-size: 1rem; opacity: 0.8; }
.bar-row {
  display: flex;
  align-items: center;
  margin: 0.4rem 0;
  gap: 0.5rem;
  font-size: 0.9rem;
}
.bar-label { min-width: 110px; text-align: right; }
.bar-label.narrow { min-width: 40px; text-align: center; font-size: 0.8rem; direction: ltr; }
.bar-track {
  flex: 1;
  background: var(--border-color, #eee);
  border-radius: 4px;
  height: 14px;
  overflow: hidden;
}
.bar-fill {
  height: 100%;
  border-radius: 4px;
  background: var(--link-color, #0070f3);
  opacity: 0.75;
}
.bar-count { min-width: 28px; text-align: left; opacity: 0.6; font-size: 0.85rem; }
</style>

<div class="stat-cards">
  <div class="stat-card">
    <span class="num">{{ total | minus: 1 }}</span>
    <span class="label">کتاب بررسی‌شده</span>
  </div>
  <div class="stat-card">
    <span class="num">{{ country_count }}</span>
    <span class="label">کشور</span>
  </div>
  <div class="stat-card">
    <span class="num">{{ avg_int }}.{{ avg_dec }}</span>
    <span class="label">میانگین امتیاز</span>
  </div>
</div>

<div class="stats-section">
<h3>ژانر</h3>

{% assign genre_max = novel_count %}
{% if short_count > genre_max %}{% assign genre_max = short_count %}{% endif %}

<div class="bar-row">
  <span class="bar-label">رمان</span>
  <div class="bar-track"><div class="bar-fill" style="width:{{ novel_count | times: 100 | divided_by: genre_max }}%"></div></div>
  <span class="bar-count">{{ novel_count }}</span>
</div>
<div class="bar-row">
  <span class="bar-label">داستان کوتاه</span>
  <div class="bar-track"><div class="bar-fill" style="width:{{ short_count | times: 100 | divided_by: genre_max }}%"></div></div>
  <span class="bar-count">{{ short_count }}</span>
</div>
<div class="bar-row">
  <span class="bar-label">غیرداستانی</span>
  <div class="bar-track"><div class="bar-fill" style="width:{{ nonfic_count | times: 100 | divided_by: genre_max }}%"></div></div>
  <span class="bar-count">{{ nonfic_count }}</span>
</div>
{% if other_count > 0 %}
<div class="bar-row">
  <span class="bar-label">سایر</span>
  <div class="bar-track"><div class="bar-fill" style="width:{{ other_count | times: 100 | divided_by: genre_max }}%"></div></div>
  <span class="bar-count">{{ other_count }}</span>
</div>
{% endif %}
</div>

<div class="stats-section">
<h3>بیشترین کشورها</h3>

{% assign top_countries = "آمریکا,انگلیس,روسیه,ژاپن,فرانسه,ایران,آرژانتین,ایتالیا,آلمان,سوئیس" | split: "," %}
{% assign c_max = site.tags['آمریکا'] | size %}

{% for c in top_countries %}
  {% assign c_count = site.tags[c] | size %}
  {% if c_count > 0 %}
<div class="bar-row">
  <span class="bar-label">{{ c }}</span>
  <div class="bar-track"><div class="bar-fill" style="width:{{ c_count | times: 100 | divided_by: c_max }}%"></div></div>
  <span class="bar-count">{{ c_count }}</span>
</div>
  {% endif %}
{% endfor %}
</div>

<div class="stats-section">
<h3>توزیع امتیاز</h3>

{% assign r_max = r7 %}
{% if r8 > r_max %}{% assign r_max = r8 %}{% endif %}

{% assign scores = "10,9,8,7,6,5,4,3,2,1" | split: "," %}
{% for s in scores %}
  {% assign rv = 0 %}
  {% if s == '10' %}{% assign rv = r10 %}
  {% elsif s == '9' %}{% assign rv = r9 %}
  {% elsif s == '8' %}{% assign rv = r8 %}
  {% elsif s == '7' %}{% assign rv = r7 %}
  {% elsif s == '6' %}{% assign rv = r6 %}
  {% elsif s == '5' %}{% assign rv = r5 %}
  {% elsif s == '4' %}{% assign rv = r4 %}
  {% elsif s == '3' %}{% assign rv = r3 %}
  {% elsif s == '2' %}{% assign rv = r2 %}
  {% elsif s == '1' %}{% assign rv = r1 %}
  {% endif %}
<div class="bar-row">
  <span class="bar-label narrow">{{ s }}/10</span>
  <div class="bar-track"><div class="bar-fill" style="width:{{ rv | times: 100 | divided_by: r_max }}%"></div></div>
  <span class="bar-count">{{ rv }}</span>
</div>
{% endfor %}
</div>
