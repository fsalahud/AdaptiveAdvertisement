(function(){
    "use strict";

    angular.module('webgallery')
        .service('imageService',function($http){

            var service = this;


            service.getDirectory = function(callback){
            console.log("enter image service"); 
            $http.get('/api/showdisplay1/')
                .success(function(data,status){
                    callback(null, data);
                })
                .error(function(error, status){
                    callback(error,null);
                });
            };

            service.getLinksys = function(callback){
            console.log("enter image service"); 
            $http.get('/api/showdisplay2/')
                .success(function(data,status){
                    callback(null, data);
                })
                .error(function(error, status){
                    callback(error,null);
                });
            };

            service.getDemographics = function(callback){
            console.log("enter image service"); 
            $http.get('/api/showdemographics/')
                .success(function(data,status){
                    callback(null, data);
                })
                .error(function(error, status){
                    callback(error,null);
                });
            };
})
})();
            