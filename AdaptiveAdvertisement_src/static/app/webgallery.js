(function(){
	"use strict";
	
	var web= angular.module('webgallery',['ngRoute']);
			// configure routes
		web.config(function($routeProvider){
            $routeProvider

                .when('/displayBarQ', {
                    templateUrl: '/static/includes/display1.html',
                    controller: 'directoryController',
                    controllerAs: 'dir'
                })
             	.when('/display', {
                    templateUrl: '/static/includes/demographics.html',
                    controller: 'demographicsController',
                    controllerAs: 'demographics'
                })

                .when('/displayLinksys', {
                    templateUrl: '/static/includes/display2.html',
                    controller: 'linksysController',
                    controllerAs: 'linksys'
                })
               
             	.otherwise({redirectTo:'/display'});
        })

		.run(["$location", "$rootScope", function ($location, $rootScope) {
             // detect url change
             $rootScope.$on('$routeChangeSuccess',function(event,current,previous){
                 // update headers
                 if(current.$$route){
                    $rootScope.title = current.$$route.title;
                    $rootScope.buttonClass = current.$$route.buttonClass;
                    $rootScope.buttonUrl = current.$$route.buttonUrl;
                }
            });

        }])

		web.controller("webgalleryController",function($http){
			console.log("hello webgalleryController!");
        });

})()