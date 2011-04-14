package com.walkr;

import android.graphics.Bitmap;

public class WalkrObject {
    private Bitmap bitmap;
    private String title;
    
    public WalkrObject(Bitmap bm, String title) {
        this.bitmap = bm;
        this.title = title;
    }
    
    public Bitmap getBitmap() {
        return bitmap;
    }
    public String getTitle() {
        return title;
    }
    
}
