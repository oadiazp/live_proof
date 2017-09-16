class @Insurance
  @add: (name) ->
     new Promise (resolve, reject) =>
        $.ajax
          url: '/api/profile/insurances/'
          method: 'post'
          data:
            name: name
            profile: PROFILE_ID
          success: (data) ->
            resolve data