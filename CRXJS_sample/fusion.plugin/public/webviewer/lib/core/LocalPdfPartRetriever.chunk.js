/** Notice * This file contains works from many authors under various (but compatible) licenses. Please see core.txt for more information. **/
(function(){(window.wpCoreControlsBundle=window.wpCoreControlsBundle||[]).push([[8],{573:function(xa,ta,h){h.r(ta);var qa=h(0);xa=h(58);var oa=h(493),na=h(271),ja=h(28),ka=window;h=function(){function fa(x){var z=this;this.Qza=function(r){return r&&("image"===r.type.split("/")[0].toLowerCase()||r.name&&!!r.name.match(/.(jpg|jpeg|png|gif)$/i))};this.file=x;this.dAa=new Promise(function(r){return Object(qa.b)(z,void 0,void 0,function(){var n;return Object(qa.d)(this,function(f){switch(f.label){case 0:return this.Qza(this.file)?
[4,Object(na.b)(x)]:[3,2];case 1:n=f.aa(),this.file=ja.q?new Blob([n],{type:x.type}):new File([n],null===x||void 0===x?void 0:x.name,{type:x.type}),f.label=2;case 2:return r(!0),[2]}})})})}fa.prototype.getFileData=function(x){var z=this,r=new FileReader;r.onload=function(n){z.trigger(fa.Events.DOCUMENT_LOADING_PROGRESS,[n.loaded,n.loaded]);x(new Uint8Array(n.target.result))};r.onprogress=function(n){n.lengthComputable&&z.trigger(fa.Events.DOCUMENT_LOADING_PROGRESS,[n.loaded,0<n.total?n.total:0])};
r.readAsArrayBuffer(this.file)};fa.prototype.getFile=function(){return Object(qa.b)(this,void 0,Promise,function(){return Object(qa.d)(this,function(x){switch(x.label){case 0:return[4,this.dAa];case 1:return x.aa(),ka.da.isJSWorker?[2,this.file.path]:[2,this.file]}})})};fa.Events={DOCUMENT_LOADING_PROGRESS:"documentLoadingProgress"};return fa}();Object(xa.a)(h);Object(oa.a)(h);Object(oa.b)(h);ta["default"]=h}}]);}).call(this || window)