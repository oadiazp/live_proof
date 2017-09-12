@ProfileController =
  extends: BaseController
  data: ->
    picture: null
    social_networks: []
    insurances: []
    first_name: null
    last_name: null
  methods:
    load: ->
      promise = new Promise (resolve, reject) ->
        $.ajax
          url: '/api/profile'
          success: (data) ->
            resolve data

      promise.then (data) =>
        @picture = data['picture']
        @social_networks = data['social_networks']
        @first_name = data['first_name']
        @last_name = data['last_name']
        @insurances = data['insurances']
  components:
    'social_network_icon': SocialNetworkIconController
    'insurance': InsuranceController
  mounted: ->
    @load()


new Vue(ProfileController).$mount '.profile_controller'
