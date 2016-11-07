/**
 * Created by shimon on 11/7/16.
 */
import {platformBrowserDynamic} from "@angular/platform-browser-dynamic";
//import {enableProdMode} from "@angular/core";
import {RegistrationModule} from "./reg.module";

//enableProdMode();
var homePage = platformBrowserDynamic();
homePage.bootstrapModule(RegistrationModule);
