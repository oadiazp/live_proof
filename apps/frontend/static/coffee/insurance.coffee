@InsuranceController =
  extends: BaseController
  template: '#insurance_template'
  props: [
    'created_humanized', 'name', 'enabled', 'id',
  ]
  methods:
    toggleStatus: ->
      promise = new Promise (resolve, reject) =>
        $.ajax
          url: "/api/profile/insurances/#{@id}/"
          method: 'patch'
          data:
            enabled: !@enabled
          success: (data) ->
            resolve data

      promise.then (data) =>
        @$emit('reload')
