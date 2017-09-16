@InsuranceModalController =
  extends: BaseController
  template: '#insurance_modal_template'
  components:
    'destination': DestinationController
  data: ->
    name: null
    destinations: []
    errors: []
    insurance_id: null
  watch:
    name: ->
      if @name
        @errors = []
  methods:
    addDestination: ->
      if not @name and @errors
        @errors.push 'Missing insurance name'
      else
        @destinations.push
          channel: null
          name: null
    save: ->
       Insurance.add(@name).then (data) =>
        destinationPromises = []
        insuranceId = data['id']

        for destination, index in @$refs.destinations
          destinationPromises.push destination.save insuranceId

        Promise.all(destinationPromises).then =>
          $('.modal').modal('hide')
          @$emit 'reload'
