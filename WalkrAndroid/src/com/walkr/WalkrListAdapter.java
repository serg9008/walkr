package com.walkr;

import java.util.Vector;

import android.app.Activity;
import android.content.Context;
import android.graphics.Bitmap;
import android.graphics.Canvas;
import android.graphics.Color;
import android.graphics.RectF;
import android.util.DisplayMetrics;
import android.view.Gravity;
import android.view.View;
import android.view.ViewGroup;
import android.view.ViewGroup.LayoutParams;
import android.widget.ArrayAdapter;
import android.widget.ImageView;
import android.widget.TableLayout;
import android.widget.TableRow;
import android.widget.TextView;

public class WalkrListAdapter extends ArrayAdapter<WalkrObject>{
	private Vector<TransparentTableLayout> layouts = new  Vector<TransparentTableLayout>();
	private Activity parentActivity;
	private int den;
	public WalkrListAdapter(int textViewResourceId, Activity a) {
		super(a, textViewResourceId);
		parentActivity = a;
		den = Main.den;
	}

	@Override
	public View getView (int p, View view, ViewGroup parent)
	{
		WalkrObject obj = this.getItem(p);
		if(layouts.size() <= p)
		{
			layouts.insertElementAt(createNewTable(parentActivity, obj.getBitmap(), obj.getTitle(), p), p );
		}
		view = layouts.elementAt(p);
		return view;
	}

	private class TransparentTableLayout extends TableLayout
	{
		public ImageView imageView;
		public TextView textView;
		public TableRow row1;

		public TransparentTableLayout(Context context)
		{
			super(context);
			row1 = new TableRow(context); 
			imageView = new ImageView(context);
			textView = new TextView(context);
			textView.setTextColor(Color.WHITE);
			this.setClickable(false);
			this.setFocusable(false);
		}

		protected void dispatchDraw(Canvas canvas) 
		{
			RectF drawRect = new RectF();
			drawRect.set(0,0, getMeasuredWidth(), getMeasuredHeight());
			canvas.drawARGB(0,0,0,0);

			super.dispatchDraw(canvas);
		}

		protected boolean onSetAlpha (int alpha)
		{
			return true;
		}
	}

	private TransparentTableLayout createNewTable(Context context, Bitmap bm, String t1, int position)
	{
		TransparentTableLayout l = new TransparentTableLayout(context);
		l.setColumnShrinkable(1, true);
		l.setColumnStretchable(1, true);


			
		l.imageView.setImageBitmap(bm);

		l.row1.setGravity(Gravity.CENTER_VERTICAL);
		l.row1.addView(l.imageView, new TableRow.LayoutParams((int) (80*den),(int) (80*den)));	            
		l.row1.addView(l.textView, new TableRow.LayoutParams(LayoutParams.FILL_PARENT, LayoutParams.FILL_PARENT));



		l.imageView.setPadding((int) (5*den),(int) (5*den),(int) (5*den),(int) (5*den));

		l.textView.setText( t1 );             
		l.textView.setTextSize((int) (25*den));
		l.textView.setLines(1);
		l.textView.setGravity(Gravity.CENTER_VERTICAL);
		l.addView(l.row1, new TableLayout.LayoutParams(LayoutParams.FILL_PARENT, LayoutParams.FILL_PARENT));

		return l;
	}
}
