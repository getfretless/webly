#!/usr/bin/env ruby
require 'cgi'
cgi = CGI.new
page = 'home'
page = cgi['page'] unless cgi['page'].empty?

puts cgi.header

greetings = ['Mr. President', 'Your Royal Majesty', 'Your Highness']
if cgi['name'].empty?
  greeting = greetings.sample
else
  greeting = cgi['name']
end

def render(page_name, &content)
  title = { 'home'  => 'Welcome', 'about' => 'About Us' }
  puts "<!doctype html><html><head><title>#{title[page_name]}</title></head><body>"
  puts yield
  puts '</body></html>'
end

render page do
  if page.downcase == 'about'
    "Hey, #{greeting}. Let me tell you about us. We are coders!"
  else
    "Hello, #{greeting}!"
  end
end
