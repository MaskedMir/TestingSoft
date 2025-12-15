package com.example.a7labatesting;

import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.ListView;

import com.example.a7labatesting.R;

import java.util.ArrayList;

public class MainActivity extends AppCompatActivity {

    private ArrayList<String> notes;
    private ArrayAdapter<String> adapter;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        notes = new ArrayList<>();
        notes.add("Первая заметка");

        ListView listView = findViewById(R.id.notes_list);
        Button addButton = findViewById(R.id.add_note_button);

        adapter = new ArrayAdapter<>(this, android.R.layout.simple_list_item_1, notes);
        listView.setAdapter(adapter);

        addButton.setOnClickListener(v -> {
            notes.add("Новая заметка " + (notes.size() + 1));
            adapter.notifyDataSetChanged();
        });
    }
}
