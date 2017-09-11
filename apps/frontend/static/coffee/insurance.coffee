@InsuranceController =
  extends: BaseController
  template: '#insurance_template'
  props: [
    'created_humanized', 'name', 'enabled', 'id'
  ]
