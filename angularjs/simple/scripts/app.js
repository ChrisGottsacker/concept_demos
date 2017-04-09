var simpleApp = angular.module('simpleApp', []);

simpleApp.controller('SimpleController', function($scope) {
		$scope.crew = ['Alex','Amos','Holden','Naomi'];
		// console.log(angular.toJson($scope.crew));
});
