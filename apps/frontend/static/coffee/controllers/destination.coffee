@DestinationController =
  extends: BaseController
  template: '#destination_template'
  props: ['index']
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
  computed:
    file_id: ->
      "file_#{@index}"
    upload_button_class: ->
      if @file
        'text-success'
      else
        'text-danger'
    is_valid: ->
      @file and @name and @channel != -1
    destination_component_error_class: ->
      if not @is_valid
        'has-error'
  methods:
    showUploadWindow: ->
      $("##{@file_id}").click()
    updateFile: (event) ->
      @file = event.target.files[0]
    save: (insuranceId) ->
      Destination.add insuranceId, @name, @channel, @file
  watch:
    name: ->
      @$emit 'destination_field_updated'
    channel: ->
      @$emit 'destination_field_updated'
    file: ->
      @$emit 'destination_field_updated'
