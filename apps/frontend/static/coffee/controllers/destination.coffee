@DestinationController =
  extends: BaseController
  template: '#destination_template'
  props: ['index']
  computed:
    file_id: ->
      "file_#{@index}"
  methods:
    showUploadWindow: ->
      $("##{@file_id}").click()
    updateFile: (event) ->
      @file = event.target.files[0]
    save: (insuranceId) ->
      Destination.add insuranceId, @name, @channel, @file
  data: ->
    name: null
    file: null
    channels: [
      {
        text: 'E-mail'
        value: 'EMAIL'
      },
      {
        text: 'Slack'
        value: 'SLACK'
      }
   ]
    channel: -1
