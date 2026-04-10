# Replaces tag link text with "FLAG country" for known Persian country names.
# Runs after each HTML page/document is rendered, targeting Chirpy's
# `post-tag` anchor elements so only tag links are affected.

COUNTRY_FLAGS = {
  'روسیه'         => '🇷🇺',
  'ایران'         => '🇮🇷',
  'برزیل'         => '🇧🇷',
  'اسپانیا'       => '🇪🇸',
  'مکزیک'         => '🇲🇽',
  'فرانسه'        => '🇫🇷',
  'آلمان'         => '🇩🇪',
  'آمریکا'        => '🇺🇸',
  'انگلستان'      => '🇬🇧',
  'انگلیس'        => '🇬🇧',
  'ژاپن'          => '🇯🇵',
  'کلمبیا'        => '🇨🇴',
  'شیلی'          => '🇨🇱',
  'آرژانتین'      => '🇦🇷',
  'سوئد'          => '🇸🇪',
  'سوئیس'         => '🇨🇭',
  'سوییس'         => '🇨🇭',
  'ایتالیا'       => '🇮🇹',
  'چین'           => '🇨🇳',
  'ترکیه'         => '🇹🇷',
  'مصر'           => '🇪🇬',
  'لهستان'        => '🇵🇱',
  'کانادا'        => '🇨🇦',
  'استرالیا'      => '🇦🇺',
  'ایرلند'        => '🇮🇪',
  'پرو'           => '🇵🇪',
  'آفریقای جنوبی' => '🇿🇦',
  'نیجریه'        => '🇳🇬',
  'کره'           => '🇰🇷',
  'سریلانکا'      => '🇱🇰',
}.freeze

# <a class="post-tag …">COUNTRY</a>  — tag pills on post cards and post pages
TAG_PILL_RE   = /<a([^>]+class="[^"]*post-tag[^"]*"[^>]*)>(%<country>s)<\/a>/

# <a class="tag" …>\n  COUNTRY<span  — tag cloud on /tags/ list page
TAG_CLOUD_RE  = /(<a[^>]+class="tag"[^>]*>)(\s*)(%<country>s)(\s*<span)/m

# <i class="fa fa-tag…"></i>\n  COUNTRY\n  <span  — h1 on individual tag archive page
TAG_H1_RE     = /(<i[^>]*fa-tag[^>]*><\/i>)(\s*)(%<country>s)(\s*<span)/m

# <td>کشور</td><td>COUNTRY</td>  — info table row in each post
TABLE_RE      = /(<td>کشور<\/td>\s*<td>)(%<country>s)(<\/td>)/

Jekyll::Hooks.register [:pages, :documents], :post_render do |doc|
  next unless doc.output_ext == '.html'
  next unless doc.output

  COUNTRY_FLAGS.each do |country, flag|
    e = Regexp.escape(country)

    doc.output = doc.output
      .gsub(Regexp.new(TAG_PILL_RE.source  % { country: e }),           "<a\\1>#{flag} #{country}</a>")
      .gsub(Regexp.new(TAG_CLOUD_RE.source % { country: e }, Regexp::MULTILINE), "\\1\\2#{flag} #{country}\\4")
      .gsub(Regexp.new(TAG_H1_RE.source    % { country: e }, Regexp::MULTILINE), "\\1\\2#{flag} #{country}\\4")
      .gsub(Regexp.new(TABLE_RE.source     % { country: e }),            "\\1#{flag} #{country}\\3")
  end
end
