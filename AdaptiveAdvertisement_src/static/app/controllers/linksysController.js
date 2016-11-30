(function(){
    "use strict";

    angular.module('webgallery')
        .controller('linksysController',function(imageService,$routeParams,$location){

   
            var t=this;

            t.data = imageService.data;

            console.log("check");
                        imageService.getLinksys(function(err, data){
                if (err) console.log(err);
                else t.data = data;
                    console.log(t.data);

            });
            setInterval(myFunc,8000);
            function myFunc(){
            imageService.getLinksys(function(err, data){
                if (err) console.log(err);
                else t.data = data;
                    console.log(t.data);

            });
        }



        });
})();

