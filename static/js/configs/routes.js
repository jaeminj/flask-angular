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

   //ng.module('app').run([$rootScope, $location, $cookieStore, $http , function ($rootScope, $location, $cookieStore, $http) {
   ng.module('app').run(['$injector', function ($rootScope, $location, $cookieStore, $http) {
        // keep user logged in after page refresh
        $rootScope.globals = $cookieStore.get('globals') || {};
        if ($rootScope.globals.currentUser) {
            $http.defaults.headers.common['Authorization'] = 'Basic ' + $rootScope.globals.currentUser.authdata; // jshint ignore:line
        }

        $rootScope.$on('$locationChangeStart', function (event, next, current) {
            // redirect to login page if not logged in and trying to access a restricted page
            var restrictedPage = $.inArray($location.path(), ['/login', '/register']) === -1;
            var loggedIn = $rootScope.globals.currentUser;
            if (restrictedPage && !loggedIn) {
                $location.path('/login');
            }
        });
    }]);


})(angular);
