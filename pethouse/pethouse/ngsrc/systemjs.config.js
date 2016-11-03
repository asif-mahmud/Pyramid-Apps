/**
 * System configuration for Angular samples
 * Adjust as necessary for your application needs.
 */
(function (global) {
  System.config({
    paths: {
      // paths serve as alias
      'npm:': 'node_modules/'
    },
    // map tells the System loader where to look for things
    map: {
      // our app is within the app folder
      homeapp: '/ngapps/home',
      // angular bundles
      '@angular/core': '/ngmodules/@angular/core/bundles/core.umd.js',
      '@angular/common': '/ngmodules/@angular/common/bundles/common.umd.js',
      '@angular/compiler': '/ngmodules/@angular/compiler/bundles/compiler.umd.js',
      '@angular/platform-browser': '/ngmodules/@angular/platform-browser/bundles/platform-browser.umd.js',
      '@angular/platform-browser-dynamic': '/ngmodules/@angular/platform-browser-dynamic/bundles/platform-browser-dynamic.umd.js',
      '@angular/http': '/ngmodules/@angular/http/bundles/http.umd.js',
      '@angular/router': '/ngmodules/@angular/router/bundles/router.umd.js',
      '@angular/forms': '/ngmodules/@angular/forms/bundles/forms.umd.js',
      // other libraries
      'rxjs':                      '/ngmodules/rxjs',
      'angular-in-memory-web-api': '/ngmodules/angular-in-memory-web-api',
    },
    // packages tells the System loader how to load when no filename and/or no extension
    packages: {
      homeapp: {
        main: './home.main.js',
        defaultExtension: 'js'
      },
      rxjs: {
        defaultExtension: 'js'
      },
      'angular-in-memory-web-api': {
        main: './index.js',
        defaultExtension: 'js'
      }
    }
  });
})(this);
