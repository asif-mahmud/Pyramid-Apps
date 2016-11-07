"use strict";
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
/**
 * Created by shimon on 11/4/16.
 */
var core_1 = require("@angular/core");
var user_1 = require("./user");
var http_1 = require("@angular/http");
require('rxjs/add/observable/throw');
require('rxjs/add/operator/map');
require('rxjs/add/operator/catch');
//import 'rxjs/add/operator/throw';
var RegistrationForm = (function () {
    function RegistrationForm(http) {
        this.http = http;
        this.user = new user_1.UserModel('', '', '', '', '');
        this.submitted = false;
        this.vstatus = { "success": false, "msg_stack": [] };
    }
    Object.defineProperty(RegistrationForm.prototype, "isEmptyName", {
        get: function () {
            if (this.user.username.trim() !== '')
                return false;
            return true;
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(RegistrationForm.prototype, "isFirstNameEmpty", {
        get: function () {
            if (this.user.first_name.trim() !== '')
                return false;
            return true;
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(RegistrationForm.prototype, "isLastNameEmpty", {
        get: function () {
            if (this.user.last_name.trim() !== '')
                return false;
            return true;
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(RegistrationForm.prototype, "isPasswordEmpty", {
        get: function () {
            if (this.user.password.trim() !== '')
                return false;
            return true;
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(RegistrationForm.prototype, "isPasswordRetypeEmpty", {
        get: function () {
            if (this.user.password_retype.trim() !== '')
                if (this.user.password === this.user.password_retype)
                    return false;
            return true;
        },
        enumerable: true,
        configurable: true
    });
    RegistrationForm.prototype.onSubmit = function () {
        var _this = this;
        var headers = new http_1.Headers({ "Content-Type": "application/json" });
        var options = new http_1.RequestOptions({ headers: headers });
        this.http.post('register', JSON.stringify(this.user), options)
            .map(function (response) { return response.json(); })
            .subscribe(function (vstatus) { return _this.vstatus = vstatus; }, function (error) { return console.log(error); });
        this.submitted = true;
        console.log(this.vstatus);
        console.log(this.diagnostic);
        return false;
    };
    Object.defineProperty(RegistrationForm.prototype, "diagnostic", {
        get: function () {
            return JSON.stringify(this.user);
        },
        enumerable: true,
        configurable: true
    });
    RegistrationForm = __decorate([
        core_1.Component({
            selector: 'registration-form',
            templateUrl: '/ngapps/registration/registration.html'
        }), 
        __metadata('design:paramtypes', [http_1.Http])
    ], RegistrationForm);
    return RegistrationForm;
}());
exports.RegistrationForm = RegistrationForm;
//# sourceMappingURL=reg.component.js.map