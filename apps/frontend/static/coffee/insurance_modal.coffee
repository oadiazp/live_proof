@InsuranceModalController =
  extends: BaseController
  template: '#insurance_modal_template'
  components:
    'destination': DestinationController
  data: ->
    name: null
    destinations: []
    channels: []
  mounted: ->
    loadChannels()
  methods:
    loadChannels: ->
      promise = new Promise (resolve, reject) ->
        $.ajax
          url: '/channels'
          success: (data) ->
            resolve data

      promise.then (data) =>
        @channels = data

    addDestination: ->
      @destinations.push
        channel: null
        id: data['id']
        name: null
