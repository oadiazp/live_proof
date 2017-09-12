@InsuranceModalController =
  extends: BaseController
  template: '#insurance_modal_template'
  components:
    'destination': DestinationController
  data: ->
    name: null
    destinations: []
  methods:
    addDestination: ->
      @destinations.push
        channel: null
        name: null
