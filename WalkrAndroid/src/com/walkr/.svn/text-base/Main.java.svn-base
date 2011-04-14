package com.walkr;


import android.app.Activity;
import android.content.Intent;
import android.graphics.BitmapFactory;
import android.os.Bundle;
import android.util.DisplayMetrics;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.EditText;
import android.widget.ImageButton;
import android.widget.ListView;
import android.widget.ViewAnimator;
import android.widget.AdapterView.OnItemClickListener;

public class Main extends Activity implements OnItemClickListener {
	private ArrayAdapter<WalkrObject> listAdapter;
	private ViewAnimator flipper;
	public static int den;
    /** Called when the activity is first created. */
    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.main);
        DisplayMetrics metrics = new DisplayMetrics();
		getWindowManager().getDefaultDisplay().getMetrics(metrics);
		den = (metrics.densityDpi / DisplayMetrics.DENSITY_DEFAULT);
		
        listAdapter = new WalkrListAdapter(android.R.layout.simple_list_item_1, this);
        flipper = (ViewAnimator) findViewById(R.id.flipper);
		ListView list = (ListView) findViewById(R.id.list01);
		listAdapter.add(new WalkrObject(BitmapFactory.decodeResource(getResources(), R.drawable.iu), "Indiana University"));
		listAdapter.add(new WalkrObject(BitmapFactory.decodeResource(getResources(), R.drawable.disney), "Disney Land"));
		listAdapter.add(new WalkrObject(BitmapFactory.decodeResource(getResources(), R.drawable.ski), "XYZ Ski Resort"));
		list.setAdapter(listAdapter);
		list.setOnItemClickListener(this);
		EditText input = (EditText) findViewById(R.id.scoreinput);
		
		ImageButton searchButton =  (ImageButton) findViewById(R.id.searchButton);
		searchButton.setImageResource(android.R.drawable.ic_search_category_default);
		list.setVerticalFadingEdgeEnabled(true);
    }
	@Override
	public void onItemClick(AdapterView<?> arg0, View arg1, int arg2, long arg3) {
		// TODO Auto-generated method stub
		Intent i = new Intent(this, WalkrMapActivity.class);
		startActivity(i);  
	}
}