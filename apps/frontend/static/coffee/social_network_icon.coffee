@SocialNetworkIconController =
  extends: BaseController
  template: '#social_network_icon_template'
  props: [
    'social_network'
  ]
  computed:
    icon: ->
      "fa fa-fw fa-#{@social_network}"

