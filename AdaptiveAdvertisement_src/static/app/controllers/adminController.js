(function(){
    "use strict";

    angular.module('webgallery')
        .directive('ngFiles', ['$parse', function ($parse) {

            function fn_link(scope, element, attrs) {
                var onChange = $parse(attrs.ngFiles);
                element.on('change', function (event) {
                    onChange(scope, { $files: event.target.files });
                });
            };

            return {
                link: fn_link
            }
        } ]);

    angular.module('webgallery')
        .controller('adminController',function(imageService,$scope,$window,$location){

            this.character = {};
            this.dragImagesource;


            this.img_url;
            var check;
            var controller = this;

            this.add_image = function(){
                if (check==2){
                    this.character.url=this.dragImagesource;
                    imageService.addImage(this.character);
                    this.character = {};
                    $location.path('/img/'+(imageService.getLen()));
                }
                else{
                    imageService.addImage(this.character);
                    this.character = {};
                    $location.path('/img/'+(imageService.getLen()));
                }   
            };

            $scope.ShowUrl = function () {
                //If DIV is visible it will be hidden and vice versa.
                $scope.urlVisible = $scope.urlVisible ? false : true;
                check=1;
            };

            $scope.ShowDrag = function () {
                //If DIV is visible it will be hidden and vice versa.
                $scope.dragVisible = $scope.dragVisible ? false : true;
                check=2;
            };

            $scope.dropzoneConfig={
                'options': { // passed into the Dropzone constructor
                    'url': 'upload.php',
                    autoProcessQueue:false,
                    maxFiles:1,
                    addRemoveLinks:true,
                    acceptedFiles:'image/*'
                },
                'eventHandlers': {
                    'thumbnail':function(file, dataUrl){
                        controller.dragImagesource=dataUrl;
                    },
                    'sending': function (file, xhr, formData) {
                    },
                    'success': function (file, response) {
                    }
                }
            }
            /*The above code for dropzone has been obtained from https://gist.github.com/compact/8118670*/
        });
})()