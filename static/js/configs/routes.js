(function (ng) {
  'use strict';

  ng.module('app').config(['$routeProvider', function ($routeProvider){
    $routeProvider
    .when('/', {
      templateUrl: '../static/partials/main.html',
      controller: 'MainController',
      controllerAs: 'main'
    })
    .when('/hello', {
      templateUrl: '../static/partials/hello.html',
      controller: 'HelloController',
      controllerAs: 'hello'
    })
    .when('/goodbye', {
      templateUrl: '../static/partials/goodbye.html',
      controller: 'GoodbyeController',
      controllerAs: 'goodbye'
    })

    .when('/login', {
        controller: 'LoginController',
        templateUrl: '../static/partials/login.view.html',
        controllerAs: 'vm'
    })

    .when('/register', {
        controller: 'RegisterController',
        templateUrl: '../static/partials/register.view.html',
        controllerAs: 'vm'
    })

    .otherwise({redirectTo: '/login'});
  }]);


})(angular);
