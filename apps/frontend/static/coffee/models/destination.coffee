class @Destination
  @add: (insuranceId, name, channel, file) ->
    new Promise (resolve, reject) ->
        data = new FormData()
        data.append 'name', name
        data.append 'channel', channel
        data.append 'file', file
        data.append 'insurance', insuranceId

        $.ajax
          url: "/api/profile/insurances/#{insuranceId}/destinations/"
          method: 'post'
          processData: false
          contentType: false
          data: data
          success: ->
            resolve()
