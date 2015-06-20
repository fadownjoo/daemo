/**
* ProjectController
* @namespace crowdsource.project.controllers
 * @author dmorina
*/
(function () {
  'use strict';

  angular
    .module('crowdsource.project.controllers')
    .controller('ProjectController', ProjectController);

  ProjectController.$inject = ['$window', '$location', '$scope', 'Project', '$filter', '$mdSidenav'];

  /**
  * @namespace ProjectController
  */
  function ProjectController($window, $location, $scope, Project, $filter, $mdSidenav) {
      var self = this;
      self.startDate = $filter('date')(new Date(), 'yyyy-MM-ddTHH:mmZ');
      self.addProject = addProject;
      self.endDate = $filter('date')(new Date(), 'yyyy-MM-ddTHH:mmZ');
      self.name = null;
      self.description = null;
      self.saveCategories = saveCategories;
      self.categories = [];
      self.getSelectedCategories = getSelectedCategories;
      self.showTemplates = showTemplates;
      self.closeSideNav = closeSideNav;

      var module = {
          serviceCharges: 0.3,
          taskAvgTime: 5,
          minWage: 12,
          minNumOfWorkers: 1,
          workerHelloTimeout: 8
      };
      self.module = module;

      self.form = {
          category: {is_expanded: false, is_done:false},
          general_info: {is_expanded: false, is_done:false},
          modules: {is_expanded: false, is_done:false},
          payment: {is_expanded: false, is_done:false},
          review: {is_expanded: false, is_done:false}
      };
      self.getPath = function(){
          return $location.path();
      };
      self.toggle = function (item) {
          Project.toggle(item);
      };
      self.categoryPool = ('Programming Painting Design Image-Labelling Writing')
          .split(' ').map(function (category) { return { name: category }; });
      activate();
      function activate(){
          Project.getCategories().then(
            function success(data, status) {
                self.categories = data.data;
            },
            function error(data, status) {
                self.error = data.data.detail;
            }).finally(function () {});
      }
      /**
       * @name addProject
       * @desc Create new project
       * @memberOf crowdsource.project.controllers.ProjectController
       */
      function addProject() {
          var project = {
              name: self.name,
              startDate: self.startDate,
              endDate: self.endDate,
              description: self.description,
              keywords: self.keywords,
              categories: Project.selectedCategories
          };
          Project.addProject(project).then(
            function success(data, status) {
                self.form.general_info.is_done = true;
                self.form.general_info.is_expanded = false;
                self.form.modules.is_expanded=true;
                //$location.path('/milestones');
            },
            function error(data, status) {
                self.error = data.data.detail;
                console.log(Project.selectedCategories);
                //$scope.form.$setPristine();
          }).finally(function () {

              });
      }
      function saveCategories() {
          self.form.category.is_expanded = false;
          self.form.category.is_done=true;
          self.form.general_info.is_expanded = true;
      }

      function getSelectedCategories(){

          return Project.selectedCategories;
      }
      function showTemplates(){
          if (self.getSelectedCategories().indexOf(3) < 0) {

          } else {
              return true;
          }
      }
      function closeSideNav(){
        $mdSidenav('right').close()
        .then(function () {
        });
      }
  }
})();