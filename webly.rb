class Webly
  def layout(page_name, &block)
    title = { 'home' => 'Welcome', 'about' => 'About Us' }
    template = File.read('layout.html.erb')
    puts ERB.new(template).result(binding)
  end

  def render_view(view_name)
    file_name = "#{view_name}.html.erb"
    if File.exist?(file_name)
      template = File.read(file_name)
      ERB.new(template).result(binding)
    else
      render_404
    end
  end

  def render_404
    File.read('404.html')
  end

  def link_to(text, url)
    "<a href=\"#{url}\">#{text}</a>"
  end
end
