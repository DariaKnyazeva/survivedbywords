app = angular.module('survivedbywords.api', ['ngResource'])

app.factory('Book', [
  '$resource', function($resource) {
    return $resource('/booksapi/:pk', { pk: '@pk' });
  }
]);

app.factory('Publisher', [
  '$resource', function($resource) {
    return $resource('/publishersapi/:pk', { pk: '@pk' });
  }
]);

app.factory('Author', [
  '$resource', function($resource) {
    return $resource('authorsapi/:pk', { pk: '@pk'});
  }
]);

app = angular.module ('survivedbywords.app.books', ['ngResource', 'angularUtils.directives.dirPagination']);

app.controller('AppController', function ($scope, $http) {
    $scope.books = [],
    $scope.totalBooks = 0,
    $scope.numPerPage = 10;  
    getResultsPage(1);

    $scope.pagination = {
        current: 1
    };

    $scope.pageChanged = function(newPage) {
        getResultsPage(newPage);
    };

    function getResultsPage(pageNumber) {
        // this is just an example, in reality this stuff should be in a service
        $http.get('/booksapi?page=' + pageNumber)
            .then(function(result) {
                $scope.books = result.data.results;
                $scope.totalBooks = result.data.count;
            });
    }
   /*
    $scope.getBooks = function() {
      $http.get('/booksapi/').then(function(result) {
	$scope.totalBooksCount = result.data.count;
        var numP = Math.ceil($scope.totalBooksCount / $scope.numPerPage);
        for(var i=1; i<=numP; i++) {      
	      	$http.get('/booksapi?page=' + i).then(function(result) {
	      	  return angular.forEach(result.data.results, function(item) {
	      	     $scope.books.push(item);
	      	  });
		 });
      	}
      });
      
    };
    $scope.getBooks(); 
*/
});


app = angular.module('survivedbywords.app.book.editor', ['survivedbywords.api', 'survivedbywords.app.books']);

app.controller('BookEditController', [
  '$scope', 'Book', function($scope, Book) {
    $scope.newBook = new Book();
    return $scope.save = function() {
      return $scope.newBook.$save().then(function(result) {
        return $scope.books.push(result);
      }).then(function() {
        return $scope.newBook = new Book();
      }).then(function() {
        return $scope.errors = null;
      }, function(rejection) {
        return $scope.errors = rejection.data;
      });
    };
  }
]);
