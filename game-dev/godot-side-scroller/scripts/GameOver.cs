using Godot;
using System;

public partial class GameOver : Control
{
	private Label gameOverText;
	private GameManager gameManager;
	
	public override void _Ready()
	{
		GetNode<Button>("/root/GameOver/VBoxContainer/PlayAgain").GrabFocus();
	}
	
	private void _on_play_again_pressed()
	{
		GetTree().ChangeSceneToFile("res://scenes/Game.tscn");
	}
	
	private void _on_quit_pressed()
	{
		GetTree().Quit();
	}
}
