using Godot;
using System;

public partial class Checkpoint : Area2D
{
	private GameManager gameManager;
	private Player player;
	
	public override void _Ready()
	{
		Connect("body_entered", new Callable(this, nameof(OnBodyEntered)));
		
		gameManager = (GameManager)GetNode("/root/GameManager");
		player = GetNode<Player>("/root/Game/Player");
		if (player == null)
		{
			GD.Print("Player not found.");
		}
	}
	
	private void OnBodyEntered(Node2D body)
	{
		if (body is Player)
		{	
			//gameManager.GotoScene("res://scenes/Level2.tscn");
			CallDeferred("SwitchToLevel2");
		}
	}
	
	private void SwitchToLevel2()
	{
		GetTree().ChangeSceneToFile("res://scenes/Level2.tscn");
	}
}
