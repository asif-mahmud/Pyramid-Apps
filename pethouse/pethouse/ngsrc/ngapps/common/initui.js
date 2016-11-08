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
var core_1 = require('@angular/core');
var InitializeDropdown = (function () {
    function InitializeDropdown(el) {
        this.el = el;
    }
    InitializeDropdown.prototype.ngOnInit = function () {
        $(this.el.nativeElement).dropdown();
    };
    InitializeDropdown.prototype.ngOnDestroy = function () {
        $(this.el.nativeElement).dropdown('destroy');
    };
    InitializeDropdown = __decorate([
        core_1.Directive({
            selector: '.ui.dropdown'
        }), 
        __metadata('design:paramtypes', [core_1.ElementRef])
    ], InitializeDropdown);
    return InitializeDropdown;
}());
exports.InitializeDropdown = InitializeDropdown;
//# sourceMappingURL=initui.js.map