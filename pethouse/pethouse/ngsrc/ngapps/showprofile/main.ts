/**
 * Created by shimon on 11/9/16.
 */
import {platformBrowserDynamic} from "@angular/platform-browser-dynamic";
import {ShowProfileApp} from "./module";

let platform = platformBrowserDynamic();
platform.bootstrapModule(ShowProfileApp);