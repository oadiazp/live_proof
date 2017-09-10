@ProfileController =
  extends: BaseController
  data: ->
    picture: null
    social_networks: []
  components:
    'social_network_icon': SocialNetworkIconController
  mounted: ->
    promise = new Promise (resolve, reject) ->
      $.ajax
        url: '/api/profile/'
        success: (data) ->
          resolve data

    promise.then (data) =>
      @picture = data['picture']
      @social_networks = data['social_networks']

new Vue(ProfileController).$mount '.profile'
