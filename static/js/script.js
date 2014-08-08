/*app = angular.module('survivedbywords.api', ['ngResource'])

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
]);*/

//app = angular.module ('survivedbywords.app.books', ['survivedbywords.api'])
app = angular.module ('survivedbywords.app.books', ['ngResource'])

/*app.controller('AppController', function($scope, Book) {
    $scope.books = Book.query();
    return $scope.books.$promise.then(function(results) {
      return angular.forEach(results, function(post) {
        return $scope.photos[post.id] = PostPhoto.query({
          post_id: post.id
        });
      });
    });
});*/

app.controller('AppController', function ($scope, $http) {
    $scope.books = []
    //$scope.books = Post.query()
    return $http.get('/booksapi/').then(function(result) {
      console.log(result.data);
      return angular.forEach(result.data.results, function(item) {
        return $scope.books.push(item);
      });
    });
});
