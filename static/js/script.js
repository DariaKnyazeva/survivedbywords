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


app = angular.module ('survivedbywords.api.lists', ['ngResource', 'angularUtils.directives.dirPagination']);

// List controller is used in Book, Publisher and Author list.
// 'Child' controllers have to override $scope.url
function ListController($scope, $http, url) {
    $scope.items = [],
    $scope.totalItems = 0,
    $scope.numPerPage = 10;  
    getResultsPage(1);

    $scope.pagination = {
        current: 1
    };

    $scope.pageChanged = function(newPage) {
        getResultsPage(newPage);
    };

    function getResultsPage(pageNumber) {
        $http.get(url + '?page=' + pageNumber)
            .then(function(result) {
                $scope.items = result.data.results;
                $scope.totalItems = result.data.count;
            });
    }
}

app = angular.module ('survivedbywords.app.books', ['survivedbywords.api.lists']);
app.controller('AppController', function ($injector, $scope, $http) {
    $injector.invoke(ListController, this, {
       $scope: $scope,
       url: '/booksapi',
       $http: $http
    });
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


app = angular.module ('survivedbywords.app.authors', ['survivedbywords.api.lists']);
app.controller('AppController', function ($injector, $scope, $http) {
    $injector.invoke(ListController, this, {
       $scope: $scope,
       url: '/authorsapi',
       $http: $http
    });
});


app = angular.module ('survivedbywords.app.publishers', ['ngResource', 'angularUtils.directives.dirPagination']);
app.controller('AppController', function ($injector, $scope, $http) {
    $injector.invoke(ListController, this, {
       $scope: $scope,
       url: '/publishersapi',
       $http: $http
    });
});
