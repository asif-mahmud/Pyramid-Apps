"use strict";
/**
 * Created by shimon on 11/4/16.
 */
var UserModel = (function () {
    function UserModel(username, first_name, last_name, password, password_retype) {
        this.username = username;
        this.first_name = first_name;
        this.last_name = last_name;
        this.password = password;
        this.password_retype = password_retype;
    }
    return UserModel;
}());
exports.UserModel = UserModel;
//# sourceMappingURL=user.js.map