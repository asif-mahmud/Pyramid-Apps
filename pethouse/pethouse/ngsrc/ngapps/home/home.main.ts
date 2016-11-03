/**
 * Created by shimon on 11/3/16.
 */
import {platformBrowserDynamic} from "@angular/platform-browser-dynamic";
//import {enableProdMode} from "@angular/core";
import {HomePageModule} from "./home.module";

//enableProdMode();
var homePage = platformBrowserDynamic();
homePage.bootstrapModule(HomePageModule);
