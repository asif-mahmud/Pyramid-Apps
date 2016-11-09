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
 * Created by shimon on 11/8/16.
 */
var core_1 = require("@angular/core");
var http_1 = require("@angular/http");
var BehaviorSubject_1 = require("rxjs/BehaviorSubject");
require("rxjs/add/operator/map");
var AddPetService = (function () {
    function AddPetService(http) {
        this.http = http;
        this._pets = new BehaviorSubject_1.BehaviorSubject([]);
        this._status = new BehaviorSubject_1.BehaviorSubject({});
        this.data_storage = {
            status: {
                success: false,
                msg_stack: []
            },
            pets: []
        };
        this.addPetUrl = '/user/add/pet';
    }
    Object.defineProperty(AddPetService.prototype, "pets", {
        get: function () {
            return this._pets.asObservable();
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(AddPetService.prototype, "status", {
        get: function () {
            return this._status.asObservable();
        },
        enumerable: true,
        configurable: true
    });
    AddPetService.prototype.load_users_pets = function (userId) {
        var _this = this;
        this.http.get("/user/" + userId + "/pets")
            .map(function (response) { return response.json(); })
            .subscribe(function (data) {
            _this.data_storage.pets = data.pets;
            _this._pets.next(Object.assign({}, _this.data_storage).pets);
        }, function (error) { return console.log(error.message); });
    };
    AddPetService.prototype.add_pet = function (pet) {
        var _this = this;
        var header = new http_1.Headers({ 'Content-Type': 'application/json' });
        var options = new http_1.RequestOptions({ headers: header });
        this.http.post(this.addPetUrl, JSON.stringify(pet), options)
            .map(function (response) { return response.json(); })
            .subscribe(function (data) {
            _this.data_storage.status = data.status;
            /*
            Insert new pet data only if success
             */
            if (_this.data_storage.status.success) {
                _this.data_storage.pets.push(data.pet);
                _this._pets.next(Object.assign({}, _this.data_storage).pets);
                _this._status.next(Object.assign({}, _this.data_storage).status);
            }
        }, function (error) { return console.log(error.message); });
    };
    AddPetService = __decorate([
        core_1.Injectable(), 
        __metadata('design:paramtypes', [http_1.Http])
    ], AddPetService);
    return AddPetService;
}());
exports.AddPetService = AddPetService;
//# sourceMappingURL=addpet.service.js.map