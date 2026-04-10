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

# Matches any <a> with class containing "post-tag" whose sole text is a country name.
TAG_LINK_RE = /<a([^>]+class="[^"]*post-tag[^"]*"[^>]*)>(%<country>s)<\/a>/

# Matches the value cell that follows a کشور (country) header cell in the info table.
TABLE_COUNTRY_RE = /(<td>کشور<\/td>\s*<td>)(%<country>s)(<\/td>)/

Jekyll::Hooks.register [:pages, :documents], :post_render do |doc|
  next unless doc.output_ext == '.html'
  next unless doc.output

  COUNTRY_FLAGS.each do |country, flag|
    escaped = Regexp.escape(country)

    tag_re   = Regexp.new(TAG_LINK_RE.source   % { country: escaped })
    table_re = Regexp.new(TABLE_COUNTRY_RE.source % { country: escaped })

    doc.output = doc.output
      .gsub(tag_re,   "<a\\1>#{flag} #{country}</a>")
      .gsub(table_re, "\\1#{flag} #{country}\\3")
  end
end
