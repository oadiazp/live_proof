@BaseController =
  delimiters: ['[[', ']]']

getCookie = (name) ->
  for cookie in document.cookie.split '; ' when cookie and name is (cookie.split '=')[0]
    return decodeURIComponent cookie[(1 + name.length)...]
  null

$.ajaxSetup
  beforeSend: (xhr, settings) ->
    unless (/^http:.*/.test settings.url) or (/^https:.*/.test settings.url)
      xhr.setRequestHeader "X-CSRFToken", getCookie 'csrftoken'
