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
    destinations_are_valid: false
  computed:
    save_button_disabled_class: ->
      if not @name or not @destinations_are_valid
        'disabled'
  watch:
    name: ->
      if @name
        @errors = []
    destinations: ->
      @updateDestinationsAreValid()
  methods:
    addDestination: ->
      if not @name and @errors
        @errors.push 'Missing insurance name'
      else
        @destinations.push
          channel: null
          name: null
        @destinations_are_valid = false
    save: ->
       Insurance.add(@name).then (data) =>
        destinationPromises = []
        insuranceId = data['id']

        for destination, index in @$refs.destinations
          destinationPromises.push destination.save insuranceId

        Promise.all(destinationPromises).then =>
          $('.modal').modal('hide')
          @$emit 'reload'
    updateDestinationsAreValid: ->
      if 'destinations' of @$refs
        console.log 123
        for destination in @$refs.destinations
          if not destination.is_valid
            @destinations_are_valid = false
            return

      @destinations_are_valid = true
