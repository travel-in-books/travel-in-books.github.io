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

Jekyll::Hooks.register [:pages, :documents], :post_render do |doc|
  next unless doc.output_ext == '.html'
  next unless doc.output

  COUNTRY_FLAGS.each do |country, flag|
    re = Regexp.new(TAG_LINK_RE.source % { country: Regexp.escape(country) })
    doc.output = doc.output.gsub(re, "<a\\1>#{flag} #{country}</a>")
  end
end
