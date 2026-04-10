# Injects a script into every HTML page that prepends a country flag emoji
# to tag links whose tag name matches a known Persian country name.

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

FLAG_SCRIPT = <<~JS.freeze
  <script>
  (function () {
    var flags = #{COUNTRY_FLAGS.to_json};
    function addFlags() {
      document.querySelectorAll('a[href*="/tags/"]').forEach(function (el) {
        if (el.dataset.flagDone) return;
        el.dataset.flagDone = '1';
        var href = el.getAttribute('href') || '';
        var raw  = href.replace(/^.*\/tags\//, '').replace(/\/$/, '');
        var name;
        try { name = decodeURIComponent(raw); } catch (e) { name = raw; }
        var flag = flags[name];
        if (!flag) return;
        // Append to last text node so icons/i-elements are unaffected.
        var nodes = el.childNodes;
        for (var i = nodes.length - 1; i >= 0; i--) {
          if (nodes[i].nodeType === 3) {
            var t = nodes[i].textContent;
            nodes[i].textContent = flag + '\u00a0' + t.replace(/^\s+/, '');
            return;
          }
        }
        el.insertAdjacentText('beforeend', '\u00a0' + flag);
      });
    }
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', addFlags);
    } else {
      addFlags();
    }
  })();
  </script>
JS

Jekyll::Hooks.register [:pages, :documents], :post_render do |doc|
  next unless doc.output_ext == '.html'
  next unless doc.output&.include?('</body>')

  doc.output = doc.output.sub('</body>', "#{FLAG_SCRIPT}</body>")
end
