(function(){
    "use strict";

    angular.module('webgallery')
        .controller('demographicsController',function(imageService,$routeParams,$location){

   
            var t=this;

            t.data = imageService.data;

            console.log("check");
                        imageService.getDemographics(function(err, data){
                if (err) console.log(err);
                else t.data = data;
                    console.log(t.data);

            });
            setInterval(myFunc,2000);
            function myFunc(){
            imageService.getDemographics(function(err, data){
                if (err) console.log(err);
                else t.data = data;
                    console.log(t.data);

            });
        console.log("repeat");
        }

        


        });
})();

